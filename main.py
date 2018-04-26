# Create by FYJ


from xml.etree.ElementTree import ElementTree, Element

def read_xml(in_path):
    '''''读取并解析xml文件
      in_path: xml路径
      return: ElementTree'''
    tree = ElementTree()
    tree.parse(in_path)
    return tree
def write_xml(tree, out_path):
  '''''将xml文件写出
    tree: xml树
    out_path: 写出路径'''
  tree.write(out_path, encoding="utf-8",xml_declaration=True)

if __name__ == "__main__":
    path = "G://get_img//ChinaVehicle2018//Annotations//"
    for a in range(0, 612):
        if a >= 0 and a < 10:
            str_0 = str(a)
            a1_list = list(str_0)
            a1_list.insert(0, '0000')
            str_01 = "".join(a1_list)
            path_1 = path + str_01 + ".xml"
            tree = read_xml(path_1)
            nodes = tree.find('./path')
            str_r = "G:\get_img\ChinaVehicle2018\JPEGImages\\" + str_01 + ".jpg"
            nodes.text = str_r
            str_o = "G://my_python_pro//ann//" + str_01 + ".xml"
            write_xml(tree, str_o)

        elif a >= 10 and a < 100:
            str_1 = str(a)
            a2_list = list(str_1)
            a2_list.insert(0, '000')
            str_02 = "".join(a2_list)
            path_2 = path + str_02 + ".xml"
            tree = read_xml(path_2)
            nodes = tree.find('./path')
            str_r1 = "G:\get_img\ChinaVehicle2018\JPEGImages\\" + str_02 + ".jpg"
            nodes.text = str_r1
            str_o1 = "G://my_python_pro//ann//" + str_02 + ".xml"
            write_xml(tree, str_o1)

        else:
            str_4 = str(a)
            a4_list = list(str_4)
            a4_list.insert(0, '00')
            str_04 = "".join(a4_list)
            path_3 = path + str_04 + ".xml"
            tree = read_xml(path_3)
            nodes = tree.find('./path')
            str_r2 = "G:\get_img\ChinaVehicle2018\JPEGImages\\" + str_04 + ".jpg"
            nodes.text = str_r2
            str_o2 = "G://my_python_pro//ann//" + str_04 + ".xml"
            write_xml(tree, str_o2)




