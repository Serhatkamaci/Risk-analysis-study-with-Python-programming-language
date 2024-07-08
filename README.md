Bu çalışmada KMeans kümeleme algoritması kullanarak Amerika Birleşik Devletleri eyaletlerinin suç istatistiklerini dört farklı gruba ayırdık. İlk olarak, veri setini yükledik ve gerekli ön işlemleri yaptık. Sonra, KElbowVisualizer aracılığıyla optimal küme sayısını belirlemek için dirsek yöntemini kullandık. Belirlenen optimal küme sayısıyla (n_clusters=4), nihai KMeans modelimizi oluşturduk.

Sonuç olarak, her eyalet için belirlenen 4 farklı küme numarası (labels) elde ettik. Bu numaraları yeniden düzenleyerek, küme merkezlerini (cluster_centers_) ve her bir küme için eyaletlerin ait olduğu küme numaralarını (labels) elde ettik.

Bu işlem, eyaletlerin suç istatistiklerine dayalı olarak benzer özelliklere sahip gruplara ayrılmasını sağlayarak, veri setindeki yapısal desenleri ve ilişkileri anlamamıza yardımcı olur.

--------------------------------------------------

In this study, we used the KMeans clustering algorithm to partition the crime statistics of the United States states into four distinct groups. Initially, we loaded the dataset and performed necessary preprocessing steps. Subsequently, we employed the KElbowVisualizer to determine the optimal number of clusters using the elbow method. With the identified optimal cluster number (n_clusters=4), we constructed our final KMeans model.

As a result, we obtained four different cluster labels (labels) for each state. Reorganizing these labels allowed us to derive the cluster centers (cluster_centers_) and determine the cluster memberships (labels) for each state.

This process facilitates the segmentation of states into groups with similar characteristics based on crime statistics, aiding in understanding structural patterns and relationships within the dataset.
