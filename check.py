import piexif

def debug_exif(image_path):
    try:
        exif = piexif.load(image_path)
        for ifd in exif:
            if ifd == "thumbnail":
                continue
            print(f"[{ifd}]")
            for tag, value in exif[ifd].items():
                tag_name = piexif.TAGS[ifd].get(tag, {}).get("name", tag)
                print(f"  {tag_name}: {value}")
    except Exception as e:
        print("读取失败:", e)

debug_exif("D:\Huawei Share\Huawei Share\gl.jpg")