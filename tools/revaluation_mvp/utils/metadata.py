def run_id(train_type: str, eval_type: str, mode: str, reliability: float, seed: int) -> str:
    return f"{train_type}__{eval_type}__{mode}__rel{reliability}__seed{seed}"
