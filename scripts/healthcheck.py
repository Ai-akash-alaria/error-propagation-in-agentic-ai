import importlib.metadata as md,platform,sys
print('Python:',sys.version)
print('System:',platform.platform())
for name in ['torch','transformers','datasets','accelerate','bitsandbytes','pytest']:
 try:print(name,md.version(name))
 except md.PackageNotFoundError:print(name,'NOT INSTALLED')
try:
 import torch
 print('CUDA available:',torch.cuda.is_available(),'MPS available:',torch.backends.mps.is_available())
 if torch.cuda.is_available():print('GPU:',torch.cuda.get_device_name(0))
except Exception as e:print('PyTorch diagnostic:',str(e))
