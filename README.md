# Jury-Instructions
The purpose of this program is to run a similarities between jury instructions. The "base" jury instruction that will be compared to other instructions is the "Civil Pattern Jury Instructions" from the Georgia Superior Court, provided by Public Resource. 
The jury instructions are uploaded from the Internet Archive and are placed into a dataframe, separated by each section of the jury instruction. The jury instructions are then placed in a natural language processing library and each cell of the dataframe is vectorized. Those vectors are placed in a new column within the dataframe; meaning that each row will have a section number, a jury instruction, and an array of vectors. Using cosine similarities, the distance between each vector is measured and compared.

On the webpage, the similar jury instructons from other jurisdictions are at least 90% similar. At the moment, only the civil pattern jury instructions for Georgia and Kansas are being compared. The goal is to include more jurisdictions and to allow different jurisdictions to be selected as the "base".

Continue to Similar Jury Instructions for <a href="https://suffolklitlab.org/Jury-Instructions/web/GeorgiaSim.html" target="_blank">Georiga</a>.

Continue to Similar Jury Instructions for <a href="https://suffolklitlab.org/Jury-Instructions/web/KansasSim.html" target="_blank">Kansas</a>.
