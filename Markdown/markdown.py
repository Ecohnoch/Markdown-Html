import readItems
import parse
import sys

def main():
    filename = sys.argv[1]
    outputname = sys.argv[2]

    allText = readItems.readSourceMD(filename)
    print(allText.split('\n'))
    html = ""
    html = html + readItems.readQuoteStyle()
    html = html + readItems.readCodeStyle()
    html = html + parse.parse(allText)
    html = html + readItems.readCodeJS()

    readItems.output(html, outputname)

if __name__ == "__main__":
    main()