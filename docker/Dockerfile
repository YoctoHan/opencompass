FROM pytorch/pytorch:2.6.0-cuda12.6-cudnn9-devel

# 设置工作目录
WORKDIR /workspace

# 设置环境变量
ENV HTTP_PROXY=http://10.103.255.1:7890
ENV HTTPS_PROXY=http://10.103.255.1:7890
ENV http_proxy=http://10.103.255.1:7890
ENV https_proxy=http://10.103.255.1:7890

# 安装必要的系统包
RUN apt-get update && apt-get install -y \
    wget \
    && rm -rf /var/lib/apt/lists/*

# 安装 Miniconda
RUN mkdir -p ~/miniconda3 && \
    wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda3/miniconda.sh && \
    bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3 && \
    rm ~/miniconda3/miniconda.sh

# 将 conda 添加到 PATH
ENV PATH="/root/miniconda3/bin:${PATH}"

# 初始化 conda
RUN /root/miniconda3/bin/conda init bash && \
    /root/miniconda3/bin/conda init --all

# 创建 conda 环境并安装 OpenCompass
RUN /root/miniconda3/bin/conda create --name opencompass python=3.10 -y && \
    /root/miniconda3/bin/conda run -n opencompass pip install "opencompass[full]"

# 设置默认激活 opencompass 环境
RUN echo "source /root/miniconda3/bin/activate" >> ~/.bashrc && \
    echo "conda activate opencompass" >> ~/.bashrc

# 设置默认 shell
SHELL ["/bin/bash", "-c"]

# 设置默认命令
CMD ["/bin/bash"]