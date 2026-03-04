import math
from collections import Counter

text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras eget lorem convallis, imperdiet est sed, congue elit. Ut tristique, dui eget tincidunt commodo, leo nibh maximus erat, vel rhoncus sapien lacus vel dui. Duis id nulla aliquet, dignissim erat vitae, pretium risus. Vestibulum id eros a tellus dapibus finibus. Nullam tempus ligula sed lectus consectetur, a venenatis metus pretium. Integer in ante ipsum. Nunc semper tortor dolor, quis facilisis purus vestibulum quis. Cras sit amet justo leo. Aenean augue sem, euismod vel nisi quis, placerat condimentum magna. Suspendisse consectetur justo in rhoncus congue. Ut gravida massa risus, et tincidunt risus fermentum eget. Ut id condimentum sem. Ut in mollis diam. Proin posuere, tortor eleifend facilisis dapibus, lectus urna molestie mi, id venenatis libero tellus vel dui. Aliquam lobortis non mauris tincidunt faucibus. Maecenas maximus nunc nisi, vel pellentesque enim mollis nec. Suspendisse potenti. Suspendisse eget nibh dignissim, dignissim est eget, efficitur quam. Phasellus vel malesuada ante. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse potenti. Ut quis enim mollis, aliquet nibh ac, pellentesque elit. Integer pulvinar pharetra ex, eget ornare purus porta ac. Cras dapibus placerat imperdiet. Sed nec leo id sem porta tempus in in risus. Curabitur sit amet suscipit nulla, vel ultricies neque. Suspendisse ac justo tincidunt, dignissim nunc vitae, pharetra nisi. Donec sollicitudin ligula orci, et egestas ex scelerisque eu. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Duis accumsan, urna ornare dapibus euismod, dolor velit molestie lectus, eget pretium velit odio in est. Nulla eget augue justo. Fusce facilisis eros at fringilla fringilla. Proin finibus pellentesque metus, ut porttitor dolor condimentum ut. Praesent interdum justo leo, vitae placerat purus tincidunt in. Ut quis mauris nec ex pulvinar suscipit. Sed at varius diam. Nunc elementum pellentesque urna, sit amet lacinia risus tempor quis. Vestibulum egestas fringilla est, in gravida dolor bibendum non. Nunc quam lectus, pellentesque ac luctus maximus, aliquet eget nisi. Aliquam finibus condimentum massa nec cursus. Pellentesque maximus vitae velit sed vehicula. Praesent bibendum lorem eu turpis faucibus pretium. Pellentesque tellus libero, molestie nec dui in, imperdiet ultricies ante. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Nullam eu odio ipsum. Vestibulum et ullamcorper ipsum. Aenean arcu lacus, eleifend eget odio ac, euismod gravida lectus. Fusce sollicitudin tempor sapien ac sollicitudin. Vivamus nunc quam, mattis nec viverra non, hendrerit ut turpis. Vivamus lobortis magna est, ultrices fermentum mauris vestibulum sed. Nulla facilisi."

total_length = len(text)

character_counts = Counter(text)

entropy = 0.0

print(f"Number of characters: {total_length}")

for char, count in character_counts.items():
    p_i = count / total_length

    print(f"  {char}: {count} -> p = {p_i:.4f}")
    
    entropy += p_i * math.log2(1 / p_i)

print(f"entropy : {entropy:.4f} bits/symbol")

