from modal import Stub, Image, Volume, Secret

N_GPUS = 4
GPU_MEM = 80
BASE_MODELS = {
    "phi-1.5": "microsoft/phi-1_5",
    # Training 70B requires experimental flag fsdp_peft_cpu_offload_for_save.
    "chat70": "meta-llama/Llama-2-70b-chat-hf",
}

image = (
    Image.micromamba()
    .micromamba_install(
        "cudatoolkit=11.8",
        "cudnn=8.1.0",
        "cuda-nvcc",
        channels=["conda-forge", "nvidia"],
    )
    .apt_install("git")
    .pip_install(
        "llama-recipes @ git+https://github.com/modal-labs/llama-recipes.git@6636910761b70ada964409960129c5a4e9c2c049",
        extra_index_url="https://download.pytorch.org/whl/nightly/cu118",
        pre=True,
    )
    .pip_install("huggingface_hub==0.17.1", "hf-transfer==0.1.3", "scipy")
    .env(dict(HUGGINGFACE_HUB_CACHE="/pretrained", HF_HUB_ENABLE_HF_TRANSFER="1"))
)

stub = Stub("llama-finetuning", image=image, secrets=[Secret.from_name("huggingface")])

# Download pre-trained models into this volume.
stub.pretrained_volume = Volume.persisted("example-pretrained-vol")

# Save trained models into this volume.
stub.results_volume = Volume.persisted("example-results-vol")

VOLUME_CONFIG = {
    "/pretrained": stub.pretrained_volume,
    "/results": stub.results_volume,
}