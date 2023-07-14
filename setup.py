import os

# env
print("FreshTemplate | by @macl2189 | github: https://github.com/EdamAme-x/FreshTemplate/")
print("\n Linux/Mac: 0 | Window: 1 \n")
t = input("OS: ")

if t == "0":
    os.system("curl -fsSL https://deno.land/x/install/install.sh | sh")
    os.system("export DENO_INSTALL=\"$HOME/.deno\"")
    os.system("export PATH=\"$DENO_INSTALL/bin:$PATH\"")
    os.system("source ~/.bashrc")
else:
    os.system("iwr https://deno.land/x/install/install.ps1 -useb | iex")

os.system("$HOME/.deno/bin/deno upgrade")  # 修正: denoコマンドのフルパスを指定

app_name = input("AppName: ")
os.system("$HOME/.deno/bin/deno run -A --no-check https://raw.githubusercontent.com/lucacasonato/fresh/main/init.ts " + app_name)  # 修正: denoコマンドのフルパスを指定
os.system("cd ./" + app_name)