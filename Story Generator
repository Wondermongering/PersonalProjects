#Script using OpenAI's API to make a story generator, outlined in scenes and arcs from a user prompt, still nead some tweaksimport openai
import os 

# Replace YOUR_API_KEY with your actual API key
openai.api_key = ""


# Get the user's prompt for the story
user_prompt = input("Enter a prompt for the story: ")

# Generate text for the story based on the prompt
model_engine = "davinci"
prompt = f"Generate a story based on the following prompt: {user_prompt}"
completions = openai.Completion.create(engine=model_engine, prompt=prompt, max_tokens=924, n=1,stop=None,temperature=0.5)
story_text = completions.choices[0].text

# Generate an outline for the story based on the generated text
prompt = f"Generate an outline for the following story:\n{story_text}"
completions = openai.Completion.create(engine=model_engine, prompt=prompt, max_tokens=924, n=1,stop=None,temperature=0.5)
outline_text = completions.choices[0].text

# Generate arcs for the outline using the OpenAI API
prompt = f"Generate arcs for the following outline:\n{outline_text}"
completions = openai.Completion.create(engine=model_engine, prompt=prompt, max_tokens=924, n=1,stop=None,temperature=0.5)
arcs_text = completions.choices[0].text

# Generate scene descriptors for the arcs using the OpenAI API
prompt = f"Generate scene descriptors for the following arcs:\n{arcs_text}"
completions = openai.Completion.create(engine=model_engine, prompt=prompt, max_tokens=924, n=1,stop=None,temperature=0.5)
scene_descriptors_text = completions.choices[0].text

# Output the generated scene descriptors
print(f"Scene Descriptors:\n{scene_descriptors_text}")

filename = "generated_story.txt"
file = open(filename, "w")
file.write(story_text)
file.close()
print(f"Generated story written to {filename}.txt")
