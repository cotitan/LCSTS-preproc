import json, xmltodict
import sys

def parse_xml_file(xml_file):
    fin = open(xml_file)
    name = xml_file.split(".")[0]
    f_src = open(name + ".article", "w")
    f_trg = open(name + ".summary", "w")

    count = 0
    xml_str = ""
    for line in fin:
        xml_str += line
        if line.strip() == "</doc>":
            xml_str = xml_str.replace(" id=%d" % count, "") \
                            .replace("&raquo", "：") \
                            .replace("<BR/>", "") \
                            .replace("<BR>", "")
            try:
                obj = xmltodict.parse(xml_str)
                article = obj["doc"]["short_text"].strip()
                summary = obj["doc"]["summary"].strip()

                f_src.write(article.replace("\n", "") + "\n")
                f_trg.write(summary.replace("\n", "") + "\n")

            except:
                print(xml_str)
            finally:
                count += 1
                xml_str = ""

    fin.close()
    f_src.close()
    f_trg.close()


if __name__ == "__main__":
    fname = sys.argv[1]
    parse_xml_file(fname)
