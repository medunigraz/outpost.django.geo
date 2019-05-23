from . import api

v1 = [
    (r"geo/background", api.BackgroundViewSet, "geo-background"),
    (r"geo/level", api.LevelViewSet, "geo-level"),
    (r"geo/rooms", api.RoomViewSet, "geo-rooms"),
    (r"geo/roomcategory", api.RoomCategoryViewSet, "geo-roomcategory"),
    (r"geo/doors", api.DoorViewSet, "geo-doors"),
    (r"geo/floors", api.FloorViewSet, "geo-floors"),
    (r"geo/buildings", api.BuildingViewSet, "geo-buildings"),
    (r"geo/nodes", api.NodeViewSet, "geo-nodes"),
    (r"geo/edgecategory", api.EdgeCategoryViewSet, "geo-edgecategory"),
    (r"geo/edges", api.EdgeViewSet, "geo-edges"),
    (r"geo/pointofinterest", api.PointOfInterestViewSet, "geo-pointofinterest"),
    (
        r"geo/pointofinterestinstance",
        api.PointOfInterestInstanceViewSet,
        "geo-pointofinterestinstance",
    ),
    (r"geo/routing/edges", api.RoutingEdgeViewSet, "geo-routing-edge"),
    (r"geo/search/rooms", api.RoomSearchViewSet, "geo-room-search"),
]
