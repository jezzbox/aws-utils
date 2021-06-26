import pandas as pd


def read_s3_file(bucket, client, key, aws_details, file_type="csv", dtype=None, sheet_name=0,index_col=None):

    file_location = f"s3://{bucket}/{client}/{key}"
    storage_options = {
        "key": aws_details["access_key_id"],
        "secret": aws_details["secret_access_key_id"],
    }
    if file_type == "csv":
        df = pd.read_csv(file_location,
                         storage_options=storage_options, dtype=dtype,
                         index_col=index_col,
                         )
        return df

    elif file_type == "xlsx" or file_type == "xls":
        df = pd.read_excel(file_location, engine="openpyxl", dtype=dtype,
                           storage_options=storage_options,
                           sheet_name=0,
                           index_col=index_col,
                           )
        return df


def write_s3_file(df, bucket, client, key, aws_details, index=False):

    file_location = f"s3://{bucket}/{client}/{key}"
    storage_options = {
        "key": aws_details["access_key_id"],
        "secret": aws_details["secret_access_key_id"],
    }

    df.to_csv(file_location,
              index=index,
              storage_options=storage_options
              )

    print("Success")
