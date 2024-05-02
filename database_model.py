import pandas as pd


def load_data():
    df = pd.read_csv("all_data.csv")
    df.Gerätezeitstempel = pd.to_datetime(df.Gerätezeitstempel)
    return df


def filter_by_user_id_and_start_stop_timestamps(df: pd.DataFrame, user_id: int, page_size: int, sort: bool, sort_ascending: bool , limit: int, start_timestamps: str = None, stop_timestamps: str = None) -> dict:
    if start_timestamps != None and stop_timestamps != None:
        filtered_df = df[(df['user_id'] == user_id)  &(df['Gerätezeitstempel'] >= start_timestamps) & (df['Gerätezeitstempel'] <= stop_timestamps)]
    else:
        filtered_df = df[df['user_id'] == user_id]

    limited_df = filtered_df.loc[0:limit]

    if sort:
        limited_df = limited_df.sort_values(by='Gerätezeitstempel', ascending=sort_ascending)

    filtered_dict = limited_df.to_dict(orient='records')
    return [filtered_dict[i:i+page_size] for i in range(0, len(filtered_dict), page_size)]

def filter_by_glucose_id(df: pd.DataFrame, glucose_id: int) -> dict:
    filtered_df = df[df['id'] == glucose_id]
    return filtered_df.to_dict(orient='records')
