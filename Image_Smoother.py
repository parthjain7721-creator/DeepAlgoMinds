class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(img), len(img[0])
        
        for r in range(ROWS):
            for c in range(COLS):
                total_sum = 0
                count = 0
                
                for dr in (-1, 0, 1):
                    for dc in (-1, 0, 1):
                        neighbor_r = r + dr
                        neighbor_c = c + dc
                        
                        if 0 <= neighbor_r < ROWS and 0 <= neighbor_c < COLS:
                            total_sum += img[neighbor_r][neighbor_c] & 255
                            count += 1
                
                smoothed_val = total_sum // count
                
                img[r][c] |= (smoothed_val << 8)
                
        for r in range(ROWS):
            for c in range(COLS):
                img[r][c] >>= 8
                
        return img