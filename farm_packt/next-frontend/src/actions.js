"use server";

import { cookies } from "next/headers";
import { getIronSession } from "iron-session";
import { sessionOptions } from "./lib";
import { redirect } from "next/navigation";

export const getSession = async () => {
  const session = await getIronSession(cookies(), sessionOptions);
  return session;
};
