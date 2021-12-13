import torch
import streamlit as st
from src.model import Model

CLASSES = [
    "Metal",
    "Paper",
    "Paperpack",
    "Plastic",
    "Plasticbag",
    "Styrofoam",
]

@st.cache
def load_model(weight:str = './model/best.pt', model_config:str='./model/model.yml'):
    if weight.endswith("ts"):
        model = torch.jit.load(weight)
    else:
        model = Model(model_config, verbose=True)
        model.load_state_dict(
            torch.load(weight, map_location=torch.device("cpu"))
        )

    return model

@torch.no_grad()
def inference(model, img, device) -> str:
    model = model.to(device)
    model.eval()
    img = img.to(device)
    pred = model(img)
    pred = torch.argmax(pred)

    return CLASSES[int(pred.detach())]