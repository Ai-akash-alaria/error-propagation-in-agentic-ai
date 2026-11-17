import pytest
from src.study import context_to_docs, corrupt, exact_match, validate_item, MockBackend, run_item
FIX={'id':'unit1','question':'What is the capital?','answer':'Paris', 'context':{'title':['France','Other'],'sentences':[['Paris is the capital of France.'],['Other context.']]}}
def test_normalization(): assert exact_match('The PARIS!','Paris') == 1
def test_corruption_deterministic_and_preserves():
 a,m=corrupt(FIX,42);b,n=corrupt(FIX,42)
 assert a==b and m==n and 'Paris is the capital of France.' in a
 assert a.count(m)==1
 assert m not in str(FIX)
def test_validation(): assert validate_item(FIX)['id']=='unit1'
def test_reject_missing():
 with pytest.raises(ValueError):validate_item({'id':'x'})
def test_pipeline_schema_mock_only():
 b=MockBackend();result=run_item(FIX,b,42)
 assert set(result['conditions'])=={'clean','injected','plain_retry','reflexion_style'}
 assert b.calls==12
 assert all(c['em'] in (0,1) for c in result['conditions'].values())
