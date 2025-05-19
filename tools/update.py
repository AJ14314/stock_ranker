input_text = """
Name                      Id                              Version      Available    Source
------------------------------------------------------------------------------------------
Amazon WorkSpaces         Amazon.WorkspacesClient         5.27.0.5408  5.27.1.5420  winget
IntelliJ IDEA 2024.3.2.2  JetBrains.IntelliJIDEA.Ultimate 2024.3.2.2   2025.1.1.1   winget
Ollama version 0.6.7      Ollama.Ollama                   0.6.7        0.6.8        winget
"""

def extract_ids_and_generate_commands(text):
    lines = text.strip().split('\n')
    commands = []
    for line in lines:
        if line.startswith('---') or line.startswith('Name') or not line.strip():
            continue
        # Extract based on fixed-width columns: name(0-26), id(26-58), version(58-73), etc.
        id_value = line[26:58].strip()
        commands.append(f"winget upgrade --include-unknown {id_value}")
    return commands

# Run the function and print the commands
for cmd in extract_ids_and_generate_commands(input_text):
    print(cmd)
