import os
import cv2
from tqdm import tqdm


origin_dir = r'D:\daily_photo\jpg'
fl = os.listdir(origin_dir)

save_dir = r'D:\daily_photo\print'


for filename in tqdm(fl):
    # print(len(filename))
  # 根据长度 截取不同位置的字段（年、月、日、时间.....）来进行注释
    if len(filename) == 21:
        # 加载背景图片
        bk_img = cv2.imread(os.path.join(origin_dir,filename))
        height, width = bk_img.shape[:2]
        # 设定字体大小和粗细的比例
        # 设置期望的文本高度为图像高度的5%
        desired_text_height = height * 0.02
        # 计算字体大小
        font_scale = cv2.getFontScaleFromHeight(cv2.FONT_HERSHEY_SIMPLEX, int(desired_text_height))
        # 设置字体粗细
        thickness = max(1, int(font_scale * 2))  # 确保粗细至少为1

        text = filename[2:10] + ' '+filename[11:13] + ':' + filename[13:15]
        # 在图片上添加文字信息
        #7: 字体大小。
        #(0, 0, 255): 这是字体颜色。
        #7: 这是线条粗细。

        # 获取文本尺寸
        (text_width, text_height), _ = cv2.getTextSize(text, cv2.FONT_HERSHEY_SIMPLEX, font_scale, thickness)

        # 设置文本位置（右下角，留出一些边距）
        margin = 10  # 边距
        text_x = width - text_width - margin
        text_y = height - margin

        # 添加文本
        bk_img = cv2.putText(bk_img, text, (text_x, text_y), cv2.FONT_HERSHEY_SIMPLEX, font_scale, (0, 0, 255), thickness, cv2.LINE_AA)
        # 显示图片
        # print(newname)
        # 保存图片
        new_filename = os.path.join(save_dir,filename)
        # print(new_filename)
        cv2.imwrite(new_filename, bk_img)
