# Gradio
Huggingface and gradio


# The basics of building a gradio app:
1. gr.Row() Places components horizontally.
2. gr.Column() Places components vertically.
3. gr.Image() Allows users to upload or draw an image.
4. gr.Slider() Enables users to select a numerical value within a specified range, making it suitable for controlling parameters such as intensity, scale, or thresholds.
5. Input field: In Gradio, an input field does not correspond to a specific component named gr.Input. Instead, it is a general term referring to any interactive component that allows the user to provide input to the application. Common input fields include gr.Textbox for text input, gr.Slider for numerical input, and gr.Image for image input. Whether a component functions as an input or an output is determined by how it is connected to the callback function (e.g., listed in the inputs or outputs argument of a .click() or .change() method), rather than by the component type itself.


In this project, I developed an interactive 'RPG(role-playing game) Character Creator' where you can create the feature of your character by yourself application using the Gradio library. I utilized the gr.Blocks API to design a custom layout, organizing the interface into specific Rows and Columns for a clean user experience. The app features various input components, including Sliders for adjusting character statistics (Strength, Magic, Speed), a Textbox for the name, and an Image uploader for the avatar. I implemented a backend Python function that processes these inputs to calculate a total 'Power Level,' dynamically assigns a character class (e.g., Warrior, Mage), and generates a formatted character sheet as the output.



# Use the huggingface transformers library and its pipelines to build a gradio app.
This application demonstrates how to use the Hugging Face transformers library and its pipelines to build a gradio app for text summarization.

It utilizes the pre-trained facebook/bart-large-cnn model within a summarization pipeline to process long articles into concise summaries. The application is designed to run on the CPU (device=-1) to ensure stability across different hardware environments. The user interface, constructed using gradio.Blocks, features adjustable sliders that allow users to control the maximum and minimum length of the generated summary dynamically.
