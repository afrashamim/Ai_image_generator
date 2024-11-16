# 🎨 Stable Diffusion Image Generator

This project leverages the 🌟 Stable Diffusion V5 model to create stunning images based on text prompts. Simply provide a description, and the AI will generate an image and save it to your desktop.

---

## ✨ Features

- 🖼️ **Text-to-Image Generation**: Create visuals from text prompts.
- 📂 **Auto-Save Images**: Saves the generated images to a unique file path on your desktop.
- 🛠️ **Customizable Prompt**: Modify prompts to create unique outputs.

---

## 📋 Requirements

### 🖥️ Prerequisites
1. **Python 3.8+** 🐍
2. **Required Packages**:
   - `torch` 🔥
   - `diffusers` 🌫️
   - `accelerate` ⚡

   Install dependencies with:
   ```bash
   pip install torch diffusers accelerate

    ```
3.**Environment Variables:**
SDV5_MODEL_PATH: Path to the pre-trained Stable Diffusion V5 model.




## 🚀 Usage

### 🛠️ Step 1: Set Up the Environment
Ensure the `SDV5_MODEL_PATH` environment variable is correctly set to the location of the model files.

#### Example:
```bash
export SDV5_MODEL_PATH="/path/to/stable-diffusion-v5"
```



### 🏃 Step 2: Run the Script
Run the Python script to generate an image:

```bash
python main.py
```

### 📁 Step 3: View the Output
Generated images will be saved to your desktop in the `SD_OUTPUT` folder.




### ⚠️ Notes  
- 📏 **Prompt Limit**: The prompt must be 200 characters or fewer.  
- 🖥️ **CPU-Based**: The script runs on CPU, which may be slower than GPU. For faster performance, switch to GPU by changing:  

```python
pipe = pipe.to("cuda")
with autocast("cuda"):
```


---



### 🔧 Further Enhancements  
- ⚡ **Enable GPU Support**: Use GPU for faster image generation.  
- 💻 **Command-Line Interface**: Allow users to input prompts and save paths via command-line arguments.  
- 🌐 **Web Interface**: Develop a user-friendly web interface for generating images.  
- 📋 **Batch Processing**: Add support to process multiple prompts at once.  
