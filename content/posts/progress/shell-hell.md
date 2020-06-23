Title: Shell Hell
Date: 2019-05-24
Modified: 2019-08-04
Lang: en
Category: Progress
Slug: progress/shell-hell
Cover: images/articles/progress/bashrc_conda.jpg
Tags: windows, bash, git bash, anaconda, virtual environments
Summary: I've been having trouble with my shells for weeks. The paths were wrong with all of them. Something to do with Anaconda.

# Several Issues

I've been having trouble with my shells for weeks. The paths were wrong with all of them. Something to do with Anaconda.

## Issue #1: Windows Command Prompt
I kept getting a message that read `"The system cannot find the path specified."`

I tried editing the `PATH` variables, but that didn't change it. Finally I found [this answer](https://superuser.com/questions/727316/error-in-command-line-the-system-cannot-find-the-path-specified) on StackExchange which said to edit the registry.

There was a path to a `conda_hook.BAT` in `HKCU\Software\Microsoft\Command Processor\AutoRun` and nothing in `HKLM\...\AutoRun`.

**Solution:** Clearing the HKCU AutoRun value cleared the prompt.

## Issue #2: Git Bash for Windows

The top of the console read `bash: $'\377\376.': command not found"`.

After spending some time examining the file structure, I noticed there was a weird looking blob of unreadable text at the beginning of `~/.bashrc` which was trying to point to `C:\Users\jzpow\Anaconda3/etc/profile.d/conda.sh`.

For the longest time, I couldn't for the life of me figure out what `'\377\376.'` was.

After learning more bash scripting, I remembered that variables were declared with `$` and could be displayed with `ECHO`, so I ran `ECHO $'\377\376.'` and out came the strange unreadable character at the beginning of the `~/.bashrc` file!

![Git Bash prompt](/images/articles/progress/bashrc_conda.jpg)

**Solution:** After clearing `~/.bashrc` and restarting the shell, the error message was gone.

## Issue #3: Windows PowerShell

PowerShell was showing the following error:

```console
. : File C:\Users\jzpow\Documents\WindowsPowerShell\profile.ps1 cannot be loaded because running scripts is disabled
on this system. For more information, see about_Execution_Policies at https:/go.microsoft.com/fwlink/?LinkID=135170.
At line:1 char:3
+ . 'C:\Users\jzpow\Documents\WindowsPowerShell\profile.ps1'
+   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : SecurityError: (:) [], PSSecurityException
    + FullyQualifiedErrorId : UnauthorizedAccess
```

After scanning the docs, I learned that PowerShell has an [execution policy](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_execution_policies?view=powershell-6) that controls running scripts and loading configuration files. In order for the scripts to be run properly, I needed to enable that functionality on the system.

Indeed, running `$ Get-ExecutionPolicy` showed `"Restricted"`. Adding `...-List` showed that all scopes were undefined, meaning there was no execution policy set on the system.

With confirmation from [this post](https://www.faqforge.com/windows/windows-powershell-running-scripts-is-disabled-on-this-system/), I ran `$ set-executionpolicy remotesigned`and saw the following error message:

```console
& : The term 'C:\Users\jzpow\Anaconda3\Scripts\conda.exe' is not recognized as the name of a cmdlet, function, script
file, or operable program. Check the spelling of the name, or if a path was included, verify that the path is correct
and try again.
At C:\Users\jzpow\Documents\WindowsPowerShell\profile.ps1:4 char:4
+ (& "C:\Users\jzpow\Anaconda3\Scripts\conda.exe" "shell.powershell" "h ...
+    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : ObjectNotFound: (C:\Users\jzpow\...ripts\conda.exe:String) [], CommandNotFoundException
    + FullyQualifiedErrorId : CommandNotFoundException
```

It looks bad, but it's actually a step in the right direction. This just means I need to initialize conda for the current shell, so I ran `$ conda init`.

Examining the output, I realized THAT'S what had changed `AutoRun` in the registry.

On top of that, I had a nice error message pop up from yet another program... Bitdefender was blocking them!! I thought that might be the case.

Here's the end of the output:

```shell
needs sudo    C:\Users\jzpow\Documents\WindowsPowerShell\profile.ps1
modified      HKEY_CURRENT_USER\Software\Microsoft\Command Processor\AutoRun
```

**Solution:** I gave Python access to change files on the system, and then ran `$ conda init powershell`, which returned this:

```shell
modified      C:\Users\jzpow\Documents\WindowsPowerShell\profile.ps1
```

Then I reopened the shell and everything ran perfectly!! :D

I'm really happy that I was able to debug these things on my own. It's very important to me to be able to work with my system by myself, navigate directories, change permissions, and fix things that are broken. If I'm going to be working with computers from here on out, I've got to get very good at figuring out what's going on when they break and how I can fix it.
