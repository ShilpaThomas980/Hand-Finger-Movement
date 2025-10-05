import numpy as np

def calculate_accuracy(finger_positions, target_path_points):
    """
    Calculate accuracy -> closeness of index finger to target path.
    finger_pos = list of (x,y) tuples for fingertip over frame.
    target_path_pos = list of (x,y) tuples defining target path / shape.
    Returns: accuracy percentage (0-100)
    """
    if not finger_positions or not target_path_points:
        return 0

    errors = []
    for fx, fy in finger_positions:
        # Find nearest point on target path
        distances = [np.hypot(fx - tx, fy - ty) for tx, ty in target_path_points]
        errors.append(min(distances))

    mean_error = np.mean(errors)

    # Convert error to accuracy
    # By adjust scaling_factor to screen / shape size
    scaling_factor = 50 # max expected distance in pixels
    accuracy = max(0, 100 - (mean_error / scaling_factor * 100))
    return accuracy
