#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# SPDX-License-Identifier: Apache-2.0
# Copyright 2022 Stéphane Caron

"""Skeleton description."""

from os import getenv as _getenv
from os import path as _path

PACKAGE_PATH = "/home/daros/Repositories/human-gazebo/humanSubjectWithSpinalCordMeshes"

URDF_PATH: str = _path.join(
    PACKAGE_PATH, "humanSubjectWithSpinalCordMeshes.urdf"
)
print("humanSubjectWithSpinalCordMeshes description URDF path:", URDF_PATH)
