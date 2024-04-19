import gradio as gr

# Define the Gradio interface
def show_external_site():
    # HTML content with an iframe referencing your external site
    html_content = """
    <iframe src="http://localhost:8000" width="100%" height="800">
        <p>Your browser does not support iframes.</p>
    </iframe>
    """
    return html_content

# Create the Gradio interface
iface = gr.Interface(
    fn=show_external_site,
    inputs=[],  # No inputs, as you're just displaying the HTML via iframe
    outputs="html"
)

# Launch the Gradio app
iface.launch()