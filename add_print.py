import os
import cv2

fl = os.listdir('D:\素材')

for filename in fl:
    print(len(filename))
  # 根据长度 截取不同位置的字段（年、月、日、时间.....）来进行注释
    if len(filename) == 16:
        # 加载背景图片
        bk_img = cv2.imread(filename)
        newname = filename[0:6] + filename[6:8] + '-' + filename[8:]
        # 在图片上添加文字信息
        bk_img = cv2.putText(bk_img, filename[0:5], (150, 150), cv2.FONT_HERSHEY_SIMPLEX, 7, (0, 0, 255), 7, cv2.LINE_AA)
        # 显示图片
        print(newname)
        # 保存图片
        cv2.imwrite(newname, bk_img)
