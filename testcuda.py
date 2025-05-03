import torch
import torchvision
import torchaudio

print("== PyTorch信息 ==")
print(f"版本: {torch.__version__}")
print(f"CUDA是否可用: {torch.cuda.is_available()}")
print(f"CUDA版本: {torch.version.cuda}")
print(f"GPU设备数: {torch.cuda.device_count()}")
if torch.cuda.is_available():
    print(f"当前GPU: {torch.cuda.current_device()}")
    print(f"设备名称: {torch.cuda.get_device_name(0)}")

print("\n== TorchVision信息 ==")
print(f"版本: {torchvision.__version__}")
print(
    f"是否支持CUDA: {'是' if torch.cuda.is_available() else '否（依赖PyTorch的CUDA）'}"
)

print("\n== TorchAudio信息 ==")
print(f"版本: {torchaudio.__version__}")
print(
    f"是否支持CUDA: {'是' if torch.cuda.is_available() else '否（依赖PyTorch的CUDA）'}"
)

# 验证GPU张量计算
if torch.cuda.is_available():
    test_tensor = torch.randn(2, 3).cuda()
    print("\n测试张量已分配至GPU:", test_tensor.device)
else:
    print("\n警告: CUDA不可用，请检查安装。")
