import pandas as pd
from sklearn.preprocessing import RobustScaler
from imblearn.over_sampling import SMOTE
import logging

# Configuração de Logs
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def remove_duplicates(df: pd.DataFrame) -> pd.DataFrame:
    """Remover linhas duplicadas do dataset."""
    initial_shape = df.shape[0]
    df = df.drop_duplicates()
    logging.info(f"Removidas {initial_shape - df.shape[0]} linhas duplicadas.")
    return df

def scale_features(df: pd.DataFrame, target_col: str = 'Class') -> pd.DataFrame:
    """
    Padroniza as colunas numéricas usando o RobustScaler, ignorando a coluna alvo.
    """
    scaler = RobustScaler()
    features = [col for col in df.columns if col != target_col]
    
    df_scaled = df.copy()
    df_scaled[features] = scaler.fit_transform(df_scaled[features])
    
    logging.info("Features numéricas foram escalonadas (RobustScaler).")
    return df_scaled

def apply_smote(X: pd.DataFrame, y: pd.Series, random_state: int = 42):
    """
    Aplica a técnica SMOTE para balanceamento da classe minoritária.
    ATENÇÃO: Deve ser aplicada apenas nos dados de TREINO.
    """
    smote = SMOTE(random_state=random_state)
    X_resampled, y_resampled = smote.fit_resample(X, y)
    
    logging.info(f"SMOTE aplicado. O dataset de treino passou de {X.shape[0]} para {X_resampled.shape[0]} linhas.")
    return X_resampled, y_resampled

def run_preprocessing_pipeline(file_path: str, target_col: str = 'Class') -> pd.DataFrame:
    """
    Exemplo de pipeline completo (apenas de limpeza).
    """
    logging.info(f"Iniciando pipeline de pré-processamento. Lendo CSV de: {file_path}")
    df = pd.read_csv(file_path)
    
    df = remove_duplicates(df)
    df = scale_features(df, target_col=target_col)
    
    logging.info("Pré-processamento base concluído.")
    return df

if __name__ == "__main__":
    # Exemplo de como rodá-lo localmente
    # df_processed = run_preprocessing_pipeline('../data/raw/creditcard.csv', target_col='Class')
    # df_processed.to_csv('../data/processed/creditcard_processed.csv', index=False)
    pass
