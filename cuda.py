# import torch
# print(torch.cuda.is_available())
# print(torch.backends.cudnn.is_available())
# print(torch.cuda_version)
# print(torch.backends.cudnn.version())
#
# # CUDA TEST
# import torch
# x = torch.Tensor([1.0])
# xx = x.cuda()
# print(xx)
#
# # CUDNN TEST
# from torch.backends import cudnn
# print(cudnn.is_acceptable(xx))
# print(torch.version.cuda)

# import torch
#
# print(torch.cuda.is_available())
# # >>> True
#
# print( torch.cuda.current_device())
# # >>> 0
#
# print(torch.cuda.device(0))
# # >>> <torch.cuda.device at 0x7efce0b03be0>
#
# print(torch.cuda.device_count())
# # >>> 1
#
# print(torch.cuda.get_device_name(0))
# # >>> 'GeForce GTX 950M'

# import torch
# print(torch.cuda.is_available())
# print(torch.backends.cudnn.is_available())
# print(torch.version.cuda)
# print(torch.version.__version__)
# print(torch.backends.cudnn.version())
#
# if torch.cuda.is_available():
#     device = torch.device("cuda:0")
#     print("running on the GPU")
# else:
#     device = torch.device("cpu")
#     print("running on the CPU")

import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
import torch.backends.cudnn as cudnn
from torchvision import datasets, transforms


class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.conv1 = nn.Conv2d(1, 10, kernel_size=5)
        self.conv2 = nn.Conv2d(10, 20, kernel_size=5)
        self.conv2_drop = nn.Dropout2d()
        self.fc1 = nn.Linear(320, 50)
        self.fc2 = nn.Linear(50, 10)

    def forward(self, x):
        x = F.relu(F.max_pool2d(self.conv1(x), 2))
        x = F.relu(F.max_pool2d(self.conv2_drop(self.conv2(x)), 2))
        x = x.view(-1, 320)
        x = F.relu(self.fc1(x))
        x = F.dropout(x, training=self.training)
        x = self.fc2(x)
        return F.log_softmax(x, dim=1)


def train(model, device, train_loader, optimizer, epoch):
    model.train()
    for batch_idx, (data, target) in enumerate(train_loader):
        data, target = data.to(device), target.to(device)
        optimizer.zero_grad()
        output = model(data)
        loss = F.nll_loss(output, target)
        loss.backward()
        optimizer.step()
        if batch_idx % 10 == 0:
            print('Train Epoch: {} [{}/{} ({:.0f}%)]\tLoss: {:.6f}'.format(
                epoch, batch_idx * len(data), len(train_loader.dataset),
                       100. * batch_idx / len(train_loader), loss.item()))

def main():
    cudnn.benchmark = True
    torch.manual_seed(1)
    device = torch.device("cuda")
    kwargs = {'num_workers': 1, 'pin_memory': True}
    train_loader = torch.utils.data.DataLoader(
        datasets.MNIST('../data', train=True, download=True,
                       transform=transforms.Compose([
                           transforms.ToTensor(),
                           transforms.Normalize((0.1307,), (0.3081,))
                       ])),
        batch_size=64, shuffle=True, **kwargs)

    model = Net().to(device)
    optimizer = optim.SGD(model.parameters(), lr=0.01, momentum=0.5)

    for epoch in range(1, 11):
        train(model, device, train_loader, optimizer, epoch)


if __name__ == '__main__':
    main()



