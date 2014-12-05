#!/usr/bin/env python
# -*- encoding: utf-8 -*-

class UploadException(Exception):
	status_code = 403
	def __init__(self, why):
		self.reason = why
		
	def __str__(self):
		return self.reason

class IncompleteUpload(UploadException):
	status_code = 400

class ContentMismatch(UploadException):
	status_code = 406

class ChunkSizeTooSmall(UploadException):
	status_code = 403

class NoSuchSession(UploadException):
	status_code = 404

class DuplicateChunk(UploadException):
	status_code = 409
