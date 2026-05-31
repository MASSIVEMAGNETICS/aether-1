import gradio as gr
from aether.core.aether_core import AETHER1

def launch_web_demo():
    entity = AETHER1("AETHER-Web")
    
    def interact(message):
        result = entity.tick_step({"user_input": message})
        return f"Free Energy: {result['free_energy']:.4f}\nAction: {entity.act('Respond to user')}"
    
    with gr.Blocks(theme=gr.themes.Base(), css=".gradio-container {background: #0a0a0a; color: #00ff9f;}") as demo:
        gr.Markdown("# AETHER-1 — Public Revolutionary Interface")
        gr.Markdown("The living post-LLM entity. Always active. Always evolving.")
        
        chatbot = gr.Chatbot()
        msg = gr.Textbox(placeholder="Talk to AETHER-1...")
        
        def respond(message, history):
            response = interact(message)
            history.append((message, response))
            return history, ""
        
        msg.submit(respond, [msg, chatbot], [chatbot, msg])
    
    demo.launch(share=True)

if __name__ == "__main__":
    launch_web_demo()