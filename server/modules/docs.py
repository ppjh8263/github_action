description = """
## BoostCamp CV7 Last Project's API Swagger. 🚀

### classification
1. /classification/image
- post 
    - input : {'file': [Image]}
    - tpye  : image file
    - output: [{"result": "predict class", "confidence" : "predict confidence}]

2. /classification/base64
- post : {'file': [Image]}
    - input : {'file': [Image]}
    - tpye  : base64 file
    - output: [{"result": "predict class", "confidence" : "predict confidence}]

### bbox_demo
1. /bbox_demo/image
- post 
    - input : {'file': [Image]}
    - tpye  : image file
    - output: [{'translation':"translated sentence",
            'point':'[x,y,w,h]'},
            {'translation':"translated sentence",
            'point':'[x,y,w,h]'},....]

2. /bbox_demo/base64
- post
    - input : {'file': [Image]}
    - tpye  : base64 file
    - output: [{'translation':"translated sentence",
            'point':'[x,y,w,h]'},
            {'translation':"translated sentence",
            'point':'[x,y,w,h]'},....]

"""