from typing import List
from collections import defaultdict


class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        """
        Group file paths by their content to find duplicates.
        Returns list of groups where each group contains >= 2 files with same content.
        """
        # Map content -> list of full file paths
        content_to_paths = defaultdict(list)

        for entry in paths:
            # Entry format: "root/dir file1(content1) file2(content2) ..."
            parts = entry.split()
            directory = parts[0]  # first token is the directory path

            # Remaining tokens are file entries like "filename(content)"
            for file_info in parts[1:]:
                # Extract filename and content (split at '(' removes the closing ')')
                # Example: "f.txt(abcd)" -> name="f.txt", content="abcd"
                name, content_with_paren = file_info.rsplit("(", 1)
                # Remove the trailing ')'
                content = content_with_paren[:-1]

                # Build full file path: directory/name
                full_path = f"{directory}/{name}"
                content_to_paths[content].append(full_path)

        # Only keep groups that have at least 2 duplicate files
        result = [paths_list for paths_list in content_to_paths.values() if len(paths_list) >= 2]
        return result