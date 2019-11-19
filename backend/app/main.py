import time
from fastapi import FastAPI, HTTPException
from starlette.requests import Request
from backend.app.file_processor import CSVProcessor
from backend.app.img_compare import ImageCompare

app = FastAPI()

@app.post('/upload')
async def process_file(request: Request):
    csv_processor = CSVProcessor()
    image_compare = ImageCompare()
    form = await request.form()
    file_name = form.get('csv_file').filename
    print(file_name)

    if not file_name:
        raise HTTPException(status_code=400, detail='malformed file content')

    contents = await form.get('csv_file').read()
    file_data = csv_processor.read_csv_data(contents)

    dict_rows = []
    for row in file_data:
        print(row)
        start = time.time()
        if not row.get('image1') or not row.get('image2'):
            print('Corrupted row: skipping')
            continue

        image1 = row.get('image1')
        image2 = row.get('image2')

        try:
            (score, diff) = image_compare.compare_ssim(image1, image2)
            if score == 1:
                err = image_compare.calculate_mse(image1, image2)
                if err == 0:
                    score = 0
            elapsed_time = time.time() - start

            write_row = {
                "image1": image1,
                "image2": image2,
                "similar": score,
                "elapsed": elapsed_time
            }

            dict_rows.append(write_row)

        except Exception as e:
            print(e)

    csv_processor.write_csv(file_name, dict_rows)
    print("CSV file written")

    return {}
