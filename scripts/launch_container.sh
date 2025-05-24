docker run --name "YoctoHan-ENGINE-73" \
           --detach \
           --ipc=host \
           --network=host \
           --gpus all \
           --shm-size=1g \
           --volume $(dirname $PWD):/workspace \
           --workdir /workspace \
           aix-opencompass-eval-250524:latest \
           tail -f /dev/null