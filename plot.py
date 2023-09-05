import pandas as pd
import matplotlib.pyplot as plt
import contextlib 
import os
from PIL import Image
import shutil

plt.rcParams['figure.max_open_warning'] = 50 

with open(os.devnull, 'w') as null_file: # to avoid print statements from MLmodel module
    with contextlib.redirect_stdout(null_file):
        from MLmodel import scaled_df
        
        df1 = pd.read_csv('final_Factors.csv')

        scaled_df['QUARTER'] =scaled_df.index.to_period('Q')
        scaled_df['QUARTER'] =scaled_df['QUARTER'].astype(str)

        for i in range(len(df1)):
            scaled_df[[df1['Factors'][i], 'CSUSHPISA']]
            grouped_data = scaled_df.groupby('QUARTER').agg({df1['Factors'][i]: 'sum', 'CSUSHPISA': 'mean'}).reset_index()
            grouped_data = grouped_data.sort_values('QUARTER')
            plt.figure(figsize=(20, 12))  # Adjust the figure size as per your preference

            plt.bar(grouped_data['QUARTER'], grouped_data[df1['Factors'][i]], label=df1['Description'][i], width=0.4, alpha=0.5, color='blue')
            plt.plot(grouped_data['QUARTER'], grouped_data['CSUSHPISA'], marker='o', linestyle='-', color='black', label='CSUSHPISA')

            plt.title(f'{df1["Description"][i]} ({df1["Factors"][i]}) \n vs \n S&P/Case-Shiller U.S. National Home Price Index CSUSHPISA (Normalized)')
            plt.xlabel('Quarter')
            plt.ylabel('Normalized Values')
            plt.legend()

            plt.grid(True)  # Add gridlines
            plt.xticks(rotation=45, ha='right')  # Rotate and align x-axis tick labels for better readability
            plt.tight_layout()
            os.makedirs('./single_images', exist_ok=True)
            plt.savefig(f'./single_images/{df1["Factors"][i]}.png', bbox_inches='tight')
            plt.close()
        #plt.show()

os.makedirs('./images', exist_ok=True)

for i in range(0, len(os.listdir('./single_images')) - 1, 2):
    image1 = Image.open(os.path.join('./single_images', os.listdir('./single_images')[i]))
    image2 = Image.open(os.path.join('./single_images', os.listdir('./single_images')[i + 1]))

    name1 = os.listdir('./single_images')[i].split('.')[0]
    name2 = os.listdir('./single_images')[i + 1].split('.')[0]

    # Get the size of the first image
    width1, height1 = image1.size

    # Get the size of the second image
    width2, height2 = image2.size

    total_width = width1 + width2

    combined_image = Image.new("RGB", (total_width, height1))

    # Paste the first image on the left
    combined_image.paste(image1, (0, 0))

    # Paste the second image on the right
    combined_image.paste(image2, (width1, 0))

    # Save the combined image to the output directory
    combined_image.save(os.path.join('./images', f"combined_{name1}_{name2}{i // 2}.png"))

shutil.rmtree('./single_images')