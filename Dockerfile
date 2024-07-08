FROM python:3.9

# 
WORKDIR /working_folder

# 
COPY ./requirements.txt /working_folder/requirements.txt

# 
RUN pip install --no-cache-dir --upgrade -r /working_folder/requirements.txt

# 
COPY ./stable_diffusion_app /working_folder/stable_diffusion_app

# 
CMD ["uvicorn", "stable_diffusion_app.main:app", "--host", "0.0.0.0", "--port", "80"]