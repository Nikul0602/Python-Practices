import argparse
import requests
def download(url,local):
    if local is None:
        local = url.split('/')[-1]

    with requests.get(url, stream = True) as r:
        r.raise_for_status()
        with open(local, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                # if chunk:
                    f.write(chunk)
    return local

parser = argparse.ArgumentParser()

#Add command line arguments

parser.add_argument('url',
                    help = "URL of the file to download:")
parser.add_argument('-o','--output',
                    help= "by which name do you want to save?", default = None)

#Parse the arguments
args = parser.parse_args()

#Use the arguments in the code

print(args.url)
print(args.output)
download(args.url, args.output)


# import argparse
# import sys
#
# from docutils.nodes import image
#
#
# def calc(args):
#     # if args.o == 'add':
#     #     return args.x + args.y
#     # elif args.o == 'sub':
#     #     return args.x - args.y
#     # elif args.o == 'mul':
#     #     return args.x * args.y
#     # elif args.o == 'div':
#     #     return args.x / args.y
#     # else:
#     #     return "wrong input"
#     pass
#
# if __name__ == '__main__':
#     parser = argparse.ArgumentParser()
#     parser.add_argument('url',
#                          help = "This is the utility for download image")
#     parser.add_argument('output',
#                          help = "by which name do you want to save?")
#
#     # parser.add_argument('--x', type=float, default = 1.0,
#     #                      help="Enter First Number. This is the utility for calculation")
#     # parser.add_argument('--y', type=float, default = 3.0,
#     #                      help="Enter First Number. ")
#     # parser.add_argument('--o', type=str, default = "add",
#     #                      help="Operation Name")
#
#     args = parser.parse_args()
#     sys.stdout.write(str(calc(args)))