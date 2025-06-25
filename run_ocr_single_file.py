from datasets import load_dataset

ds = load_dataset("iiit5k", split="test")
sample = ds[0]                # 任意取一筆資料
img = sample["image"].path    # 圖片檔案路徑

