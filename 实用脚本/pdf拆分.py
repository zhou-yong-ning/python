from PyPDF2 import PdfReader, PdfWriter
import os


def split_pdf(input_path, page_numbers, path):
    input_pdf = PdfReader(input_path)
    for page_number in page_numbers:
        output_pdf = PdfWriter()
        output_pdf.add_page(input_pdf.pages[(page_number - 1)])  # 页码从0开始，所以需要减1
        output_path = os.path.join(path, input_path.split('.')[0] + '_' + str(page_number) + '.pdf')  # 拆分后的文件名
        with open(output_path, "wb") as output_file:
            print(input_path, "第", page_number, '页，拆分完成！')
            output_pdf.write(output_file)


def get_pdf_page_count(file_path):
    pdf = PdfReader(file_path)
    page_count = len(pdf.pages)
    return page_count


# 在当前路径创建文件夹
Current_Folder_path = os.getcwd()
if not os.path.exists(Current_Folder_path + '\\NewFolder'):
    os.mkdir(os.path.join(Current_Folder_path, 'NewFolder'))

# 提取后缀为pdf的文件
file_list = os.listdir(Current_Folder_path)
pdf_list = [a for a in file_list if a.endswith('.pdf')]
# 指定输入路径
for i in pdf_list:
    pdfpath = os.path.join(Current_Folder_path, 'NewFolder')
    # # 指定要拆分的页码
    # pages_to_split = [2, 5, 7]
    # 所有页码拆分
    pages_to_split = [i for i in range(1, 1 + get_pdf_page_count(i))]
    # 调用pdf拆分函数
    split_pdf(i, pages_to_split, pdfpath)
