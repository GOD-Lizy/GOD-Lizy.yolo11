# Ultralytics YOLO 🚀, AGPL-3.0 license

import math

import cv2

from ultralytics.solutions.solutions import BaseSolution  # Import a parent class
from ultralytics.utils.plotting import Annotator, colors


class DistanceCalculation(BaseSolution):
    """A class to calculate distance between two objects in a real-time video stream based on their tracks."""

    def __init__(self, **kwargs):
        """Initializes the DistanceCalculation class with the given parameters."""
        super().__init__(**kwargs)

        # Mouse event information
        self.left_mouse_count = 0
        self.selected_boxes = {}

    def mouse_event_for_distance(self, event, x, y, flags, param):
        """
        Handles mouse events to select regions in a real-time video stream.

        Args:
            event (int): Type of mouse event (e.g., cv2.EVENT_MOUSEMOVE, cv2.EVENT_LBUTTONDOWN, etc.).
            x (int): X-coordinate of the mouse pointer.
            y (int): Y-coordinate of the mouse pointer.
            flags (int): Flags associated with the event (e.g., cv2.EVENT_FLAG_CTRLKEY, cv2.EVENT_FLAG_SHIFTKEY, etc.).
            param (dict): Additional parameters passed to the function.
        """
        if event == cv2.EVENT_LBUTTONDOWN:
            self.left_mouse_count += 1
            if self.left_mouse_count <= 2:
                for box, track_id in zip(self.boxes, self.track_ids):
                    if box[0] < x < box[2] and box[1] < y < box[3] and track_id not in self.selected_boxes:
                        self.selected_boxes[track_id] = box

        elif event == cv2.EVENT_RBUTTONDOWN:
            self.selected_boxes = {}
            self.left_mouse_count = 0

    def calculate(self, im0):
        """
        Processes the video frame and calculates the distance between two bounding boxes.

        Args:
            im0 (ndarray): The image frame.

        Returns:
            (ndarray): The processed image frame.
        """
        self.annotator = Annotator(im0, line_width=self.line_width)  # Initialize annotator
        self.extract_tracks(im0)  # Extract tracks

        # Iterate over bounding boxes, track ids and classes index
        for box, track_id, cls in zip(self.boxes, self.track_ids, self.clss):
            self.annotator.box_label(box, color=colors(int(cls), True), label=self.names[int(cls)])

            if len(self.selected_boxes) == 2:
                for trk_id in self.selected_boxes.keys():
                    if trk_id == track_id:
                        self.selected_boxes[track_id] = box

        if len(self.selected_boxes) == 2:
            # Store user selected boxes in centroids list
            self.centroids.extend(
                [[int((box[0] + box[2]) // 2), int((box[1] + box[3]) // 2)] for box in self.selected_boxes.values()]
            )
            # Calculate pixels distance
            pixels_distance = math.sqrt(
                (self.centroids[0][0] - self.centroids[1][0]) ** 2 + (self.centroids[0][1] - self.centroids[1][1]) ** 2
            )
            self.annotator.plot_distance_and_line(pixels_distance, self.centroids)

        self.centroids = []

        self.display_output(im0)  # display output with base class function
        cv2.setMouseCallback("Ultralytics Solutions", self.mouse_event_for_distance)

        return im0  # return output image for more usage