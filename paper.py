import requests
import hashlib

# #Get all Minecraft Versions
# versData = requests.get("https://api.papermc.io/v2/projects/paper")
# vers = dict(versData.json())['versions']
# print(vers)

def Download(ver):
    #Use Version to get papermc builds
    buildsDatas = requests.get(f"https://api.papermc.io/v2/projects/paper/versions/{ver}/builds")
    buildsData = dict(buildsDatas.json())['builds']

    NewestBuild = buildsData[-1]['build']
    #Get File Name
    File = buildsData[-1]['downloads']['application']['name']
    ShaHash = buildsData[-1]['downloads']['application']['sha256']
    print("Downloading " + File)

    #Download
    Download = f"https://api.papermc.io/v2/projects/paper/versions/{ver}/builds/{NewestBuild}/downloads/{File}"
    PaperFile = requests.get(Download)
    open(File, "wb").write(PaperFile.content)

    #Check Hash(Sha256)
    with open(File,"rb") as f:
        bytes = f.read()
        FileHash = hashlib.sha256(bytes).hexdigest()
    if ShaHash == FileHash:
        print("Download Complete")
        Done = True
        exit(0)
    else:
        print("Download Error, Redownloading!")

if __name__ == "__main__":
    Done = False
    while Done == False:
        Download("1.18.2")
