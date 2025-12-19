# Gradio
Huggingface and gradio


The basics of building a gradio app:
1. gr.Row() Places components horizontally.
2. gr.Column() Places components vertically.
3. gr.Image() Allows users to upload or draw an image.
4. gr.Slider() Enables users to select a numerical value within a specified range, making it suitable for controlling parameters such as intensity, scale, or thresholds.
5. Input field: In Gradio, an input field does not correspond to a specific component named gr.Input. Instead, it is a general term referring to any interactive component that allows the user to provide input to the application. Common input fields include gr.Textbox for text input, gr.Slider for numerical input, and gr.Image for image input. Whether a component functions as an input or an output is determined by how it is connected to the callback function (e.g., listed in the inputs or outputs argument of a .click() or .change() method), rather than by the component type itself.





