import gzip

with open('modeling_data.pkl', 'rb') as f_in, gzip.open('modeling_data.gz', 'wb') as f_out:
    f_out.writelines(f_in)
