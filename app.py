import gradio as gr
from transformers import pipeline

# use CPU (device=-1)
summarizer = pipeline(
    "summarization",
    model="facebook/bart-large-cnn",
    device=-1 
)

def summarize_text(text: str, max_len: int, min_len: int):
    print(f"\n--- new request ---")
    if not text.strip():
        return "please input the article"

    try:
        print("please wait for 20 seconds or more")
        # incase of error
        result = summarizer(text, max_length=max_len, min_length=min_len, do_sample=False)
        summary = result[0]["summary_text"]
        print(f"output: {summary[:20]}...")
        return summary
    except Exception as e:
        print(f"error {e}")
        return f"error: {e}"

with gr.Blocks(title=" my summary") as demo:
    gr.Markdown("# your summary") 
    
    with gr.Row():
        with gr.Column():
            text_input = gr.Textbox(lines=10, label="please input the aritcle")
            max_len = gr.Slider(50, 150, value=60, label="max length")
            min_len = gr.Slider(10, 50, value=20, label="min length")
            btn = gr.Button("summary)")
        with gr.Column():
            output = gr.Textbox(lines=6, label="summary")

    btn.click(summarize_text, inputs=[text_input, max_len, min_len], outputs=output)

if __name__ == "__main__":
    demo.launch()