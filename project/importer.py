# Install yfinance package.
# pip install yfinance
 
# Import yfinance
import yfinance as yf
import os

ticks = [
    "ABEV3.SA",
    "AZUL4.SA",
    "B3SA3.SA",
    "BBAS3.SA",
    "BBDC3.SA",
    "BBDC4.SA",
    "BBSE3.SA",
    "BPAC11.SA",
    "BRAP4.SA",
    "BRDT3.SA",
    "BRFS3.SA",
    "BRKM5.SA",
    "BRML3.SA",
    "BTOW3.SA",
    "CCRO3.SA",
    "CIEL3.SA",
    "CMIG4.SA",
    "COGN3.SA",
    "CSAN3.SA",
    "CSNA3.SA",
    "CVCB3.SA",
    "CYRE3.SA",
    "ECOR3.SA",
    "EGIE3.SA",
    "ELET3.SA",
    "ELET6.SA",
    "EMBR3.SA",
    "ENBR3.SA",
    "EQTL3.SA",
    "FLRY3.SA",
    "GGBR4.SA",
    "GNDI3.SA",
    "GOAU4.SA",
    "GOLL4.SA",
    "HYPE3.SA",
    "IGTA3.SA",
    "IRBR3.SA",
    "ITSA4.SA",
    "ITUB4.SA",
    "JBSS3.SA",
    "KLBN11.SA",
    "LAME4.SA",
    "LREN3.SA",
    "MGLU3.SA",
    "MRFG3.SA",
    "MRVE3.SA",
    "MULT3.SA",
    "NATU3.SA",
    "PCAR4.SA",
    "PETR3.SA",
    "PETR4.SA",
    "QUAL3.SA",
    "RADL3.SA",
    "RAIL3.SA",
    "RENT3.SA",
    "SANB11.SA",
    "SBSP3.SA",
    "SMLS3.SA",
    "SUZB3.SA",
    "TAEE11.SA",
    "TIMP3.SA",
    "UGPA3.SA",
    "USIM5.SA",
    "VALE3.SA",
    "VIVT4.SA",
    "VVAR3.SA",
    "WEGE3.SA",
    "YDUQ3.SA"
]
for tick in ticks:
    fileDir = os.getcwd() + "/data/"
    fileName = tick+'.txt'
    fileFullPath = os.path.join(fileDir, fileName)
    if not os.path.isfile(fileFullPath):
        # Get the data for the stock Apple by specifying the stock ticker, start date, and end date
        data = yf.download(tick,'2016-01-01','2018-01-01')
        data.to_csv(fileFullPath, header=None, index=None, sep=' ', mode='a')