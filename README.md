## Tired of sharp edges in Alacritty in Windows? Want to touch a blur and roundness?

This repository is your one-stop shop for transforming your Alacritty window on Windows!

## Why This Repo?

While Alacritty offers a ton of customization options, the blur feature is currently limited to macOS. But fear not! This guide will show you how to achieve a delightful blur and rounded corners effect on your Windows machine.

By the way This project is built upon the fantastic work of XP20 and his [alacritty-background-blur](https://github.com/XP20/alacritty-background-blur). His innovative approach to background blur in Alacritty provided a strong foundation for this project.

## Before You Begin: A Gentle Reminder

I understand the hesitation to run scripts from unfamiliar sources. That's why i encourage you to take a peek at the code before diving in. Here's a quick rundown of what each script does:

- **bluralacritty.py**: This is the hero of the show! It applies the blur and rounded corner magic to your Alacritty window.
- **blurala.py**: This script helps create a handy executable file, making the process even smoother.

Feel free to explore the code and understand its functionality before proceeding.

## Getting Started (Choose Your Adventure!)

You can clone this repo or just download the script manually, it's up to you alright.

### A Note on Opacity

To achieve the best blur effect, you'll need to enable opacity in your Alacritty configuration. Set the opacity value to something low (e.g., 0.6) to allow the blur to shine through.

### Testing

Before diving into the setup process, let's make sure everything works as expected. Open Alacritty and run the bluralacritty.py script. If you see your Alacritty window adorned with a beautiful blur and rounded corners, you're good to go!

But what if you close and reopen Alacritty? The blur and rounded effect might vanish. Don't worry, we have a solution for that!

### Making it Stick

Wouldn't it be amazing if you could run the script with a single command every time you open Alacritty? We hear you! Here's how to create an executable file and add it to your system's PATH:

1. **Crafting the Executable**: Open your terminal and navigate to the directory containing the scripts. Then, run the following command:

```bash
pyinstaller --onefile blurala.py
```

This will create a new directory called dist containing the executable file named blurala.exe.

2. **Adding it to Your PATH**: Now, you need to move the blurala.exe file to a directory that's included in your system's PATH environment variable. This allows you to access the executable from any location in your command prompt. (Note: You might need administrator privileges for this step.). A common location for system-wide executables is C:\Windows

3. **Testing the Macgic**: Press Windows Key + R to open the Run dialog. Then, type blurala and press Enter.

Voila! If everything went smoothly, the blur and rounded corner effect script should run, transforming your Alacritty window every time you use the custom command.

i hope this guide empowers you to create a more visually appealing Alacritty experience on Windows! If you have any questions or encounter any issues, feel free to reach out.

