import tensorflow as tf
from stable_baselines3 import PPO
from stable_baselines3.common.envs import DummyVecEnv
from trading_env import TradingEnv  # Custom environment

def train_lstm_model(X_train, y_train):
    model = tf.keras.Sequential([
        tf.keras.layers.LSTM(50, input_shape=(X_train.shape[1], 1)),
        tf.keras.layers.Dense(1)
    ])
    model.compile(optimizer='adam', loss='mse')
    model.fit(X_train, y_train, epochs=20, batch_size=32)
    return model

def train_rl_agent(df):
    env = DummyVecEnv([lambda: TradingEnv(df)])
    model = PPO('MlpPolicy', env, verbose=1)
    model.learn(total_timesteps=10000)
    return model
