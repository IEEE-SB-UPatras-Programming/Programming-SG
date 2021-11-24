#include "olcPixelGameEngine.h"
#include "olcPGEX_RayCastWorld.h"


class ExampleGame : public olc::rcw::Engine
{
public:
    ExampleGame(const int screen_w, const int screen_h, const float fov) : Engine(screen_w, screen_h, fov)
    {

            sMap =
			"################################################################"
			"#.........#....................##..............................#"
			"#.........#....................................................#"
			"#.........#....................................................#"
			"#.........#....................................................#"
			"#.........#############........................................#"
			"#...............#..............................................#"
			"#...............#..............................................#"
			"#...............#..............................................#"
			"#.....#..#..#...#..............................................#"
			"#...............#..............................................#"
			"#...............#..............................................#"
			"#.....#..#..#..................................................#"
			"#..............................................................#"
			"#..............................................................#"
			"#..............................................................#"
			"#..............................................................#"
			"#.....................######..#................................#"
			"#.....................#.......#................................#"
			"#....................##.###.###.........................#......#"
			"#....................##.....#........................##........#"
			"#....................##.#####........................##.#......#"
			"#....................#.#.......................................#"
			"#....................#..#...............................#......#"
			"#..............................................................#"
			"#..............................................................#"
			"#..............................................................#"
			"#..............................................................#"
			"#..............................##..............................#"
			"#..............................##..............................#"
			"#..............................##..............................#"
			"################################################################";

            vWorldSize = {64, 32};
    }


    virtual olc::Pixel SelectSceneryPixel(const int tile_x, const int tile_y, const olc::rcw::Engine::CellSide side, const float sample_x, const float sample_y, const float distance) 
    {

        olc::Pixel p = olc::BACK;

        switch (side)
        {
            case olc::rcw::Engine::CellSide::Top:
                p = olc::CYAN;
                break;
            
            case olc::rcw::Engine::CellSide::Bottom:
                p = olc::GREEN;
                break;
            default:
                p = olc::WHITE;
        }

        float fDistance = 1.0f - std::min(distance/32.0f, 1.0f);

        float fShadow = 1.0f;

        switch (side)
        {
            case olc::rcw::Engine::CellSide::South: fShadow = 0.3f; break;
            case olc::rcw::Engine::CellSide::East: fShadow = 0.3f; break;
        }

        p.r *= fDistance * fShadow;
        p.g *= fDistance * fShadow;
        p.b *= fDistance * fShadow;

        return p;
    }

    virtual bool IsLocationSolid(const float tile_x, const float tile_y)
    {
        if (tile_x >= 0 && int(tile_x) < vWorldSize.x && tile_y >= 0 && int(tile_y) < vWorldSize.y)
            return sMap[int(tile_x) + vWorldSize.x * int(tile_y)] == '#';

        return true;
    }

    virtual float GetObjectWidth(const uint32_t id)
    {
        return 1;
    }
    virtual float GetObjectHeight(const uint32_t id) 
    {
        return 1;
    }

    virtual olc::Pixel SelectObjectPixel(const uint32_t id, const float sample_x, const float sample_y, const float distance, const float angle)
    {
        auto p = olc::BACK;

        return p;
    }

private:

    std::string sMap;
    olc::vi2d vWorldSize;
};

// Override base class with your custom functionality
class Example : public olc::PixelGameEngine
{
public:
	Example()
	{
		// Name your application
		sAppName = "Example";
	}

public:
	bool OnUserCreate() override
	{

        pGame.reset( new ExampleGame(ScreenWidth(), ScreenHeight(), 1) );

        auto player = std::make_shared<olc::rcw::Object>();
        player -> pos = {2.0f, 2.0f};
        player -> bVisible = false;

        pGame -> mapObjects[0] = player;



		return true;
	}

	bool OnUserUpdate(float fElapsedTime) override
	{
        auto& player = pGame -> mapObjects[0];

        if (GetKey(olc::Key::A).bHeld) // Turn Left
			player->Turn(-fPlayerMoveSpeed * 0.1f * fElapsedTime);
		
		if (GetKey(olc::Key::D).bHeld) // Turn Right
			player->Turn(+fPlayerMoveSpeed * 0.1f * fElapsedTime);

        player -> Stop();

        // Walk Forward
		if (GetKey(olc::Key::W).bHeld) player->Walk(+fPlayerMoveSpeed);
		// Walk Backwards
		if (GetKey(olc::Key::S).bHeld) player->Walk(-fPlayerMoveSpeed);
		// Strafe Right
		if (GetKey(olc::Key::E).bHeld) player->Strafe(+fPlayerMoveSpeed);
		// Strafe Left
		if (GetKey(olc::Key::Q).bHeld) player->Strafe(-fPlayerMoveSpeed);

        pGame -> Update(fElapsedTime);

        pGame -> SetCamera(player -> pos, player -> fHeading);

        pGame -> Render();

		return true;
	}
private:

    std::unique_ptr<ExampleGame> pGame = nullptr;
    float fPlayerMoveSpeed = 16.0f;
};

int main()
{
	Example demo;
	if (demo.Construct(300, 300, 4, 4))
		demo.Start();
	return 0;
}

