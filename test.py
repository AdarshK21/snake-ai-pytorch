import os

@staticmethod    
def list_saved_models():
    model_folder_path = 'G:/GITHUB REPOS/snake-ai-pytorch/saved_models'
    if not os.path.exists(model_folder_path):
        print("No models saved yet.")
    else:
        saved_models = [f for f in os.listdir(model_folder_path) if f.endswith('.pkl')]
        if saved_models:
            print("Saved models:")
            for model in saved_models:
                print(model)
        else:
            print("No models saved yet.")

list_saved_models()
