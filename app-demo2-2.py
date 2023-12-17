import gradio as gr

def generate_text(title, context):
    return f"Title:{title}\nContext:{context}\n..."

def generate_mutimodal(title, context, img):
    return f"Title:{title}\nContext:{context}\n...{img}"

with gr.Blocks() as demo:
    gr.Markdown("# 多模态可控XX生成")

    with gr.Tabs():

        with gr.TabItem("新闻输入"):
            title = gr.Textbox(label="标题", lines=1, placeholder="请输入标题")
            context = gr.Textbox(label="正文", lines=2, placeholder="请输入正文")
            text_button = gr.Button("生成")
            
            text_output = gr.Textbox(label="生成内容", lines=5, placeholder="生成列表")


        with gr.TabItem("图文输入"):
            title2 = gr.Textbox(label="标题", lines=1, placeholder="请输入标题")
            context2 = gr.Textbox(label="正文", lines=2, placeholder="请输入正文")
            img = gr.Image(label="请上传图片")
            img_button = gr.Button("生成")

            img_output = gr.Textbox(label="生成内容", lines=5, placeholder="生成列表")


    text_button.click(fn=generate_text, inputs=[title,context], outputs=text_output)
    img_button.click(fn=generate_mutimodal, inputs=[title2,context2,img], outputs=img_output)

demo.launch()
